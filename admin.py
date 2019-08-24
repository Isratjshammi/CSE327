import os
from exception import Error
from productsData import ProductsData

UPLOAD_FOLDER = './static/images/'
ALLOWED_EXTENSIONS = {'png', }


def admin_perform_query(action, form, target_category_id, target_product_id, product, picture):
    if action == "update_category_id":
        product.update_category('categoryID', form['category_id'], target_category_id)
        rename_image("category_id", UPLOAD_FOLDER, target_category_id, form['category_id'], None)
    elif action == "update_category_name":
        product.update_category('categoryName', form['category_name'], target_category_id)
    elif action == "change_product_category":
        product.update_product_details('categoryID', form['category_id'], target_category_id, target_product_id)
        rename_image("particular", UPLOAD_FOLDER, target_category_id, form['category_id'], target_product_id)
    elif action == "update_product_id":
        product.update_product_details('productID', form['product_id'], target_category_id, target_product_id)
        rename_image("product_id", UPLOAD_FOLDER, target_product_id, form['product_id'], target_category_id)
    elif action == "update_name":
        product.update_product_details('name', form['name'], target_category_id, target_product_id)
    elif action == "update_price":
        product.update_product_details('price', form['price'], target_category_id, target_product_id)
    elif action == "update_cost":
        product.update_product_details('cost', form['cost'], target_category_id, target_product_id)
    elif action == "update_quantity":
        product.update_product_details('quantityLeft', form['quantity_left'],
                                       target_category_id, target_product_id)
    elif action == 'add_category':
        product.add_category(form['category_id'], form['category_name'])
    elif action == 'delete_category':
        product.delete_category(form['category_id'])
    elif action == 'add_product':
        admin_add_product(form, picture, UPLOAD_FOLDER, ALLOWED_EXTENSIONS)
    elif action == 'update_image':
        upload_file(picture, UPLOAD_FOLDER, ALLOWED_EXTENSIONS, form['category_id'], form['product_id'])


def admin_add_product(form, picture, upload_folder, allowed_extensions):
    product = ProductsData.new_product(form['category_id'], form['product_id'], form['name'],
                                       form['price'], form['cost'], form['quantity'])
    product.add_product()
    upload_file(picture, upload_folder, allowed_extensions, form['category_id'], form['product_id'])


def allowed_file(filename, allowed_extensions):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions


def upload_file(file, upload_folder, allowed_extensions, category_id, product_id):
    if file.filename == '':
        raise Error("Picture not included")
    if file and allowed_file(file.filename, allowed_extensions):
        filename = f"{category_id}_{product_id}.png"
        file.save(os.path.join(upload_folder, filename))
        return True
    else:
        raise Error("Picture upload not Complete")


def rename_image(target, folder, old_id, new_id, additional_id):
    for file_name in os.listdir("./static/images"):
        filename = file_name.strip(".png")
        filename = filename.split("_")
        if target == "category_id":
            if filename[0] == old_id:
                target_file = os.path.join(folder, f"{new_id}_{filename[1]}.png")
                source_file = os.path.join(folder, file_name)
                os.rename(source_file, target_file)
        elif target == "product_id":
            if filename[0] == additional_id and filename[1] == old_id:
                target_file = os.path.join(folder, f"{filename[0]}_{new_id}.png")
                source_file = os.path.join(folder, file_name)
                os.rename(source_file, target_file)
                break
        elif target == "particular":
            if filename[0] == old_id and filename[1] == additional_id:
                target_file = os.path.join(folder, f"{new_id}_{filename[1]}.png")
                source_file = os.path.join(folder, file_name)
                os.rename(source_file, target_file)
                break
