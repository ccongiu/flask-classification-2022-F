from flask import render_template, request # Request is employed for allowing the image upload
from PIL import Image # PIL is employed for managing the images
from app import app
from app.forms.classification_on_uploaded_form import ClassificationUploadForm
from ml.classification_utils import classify_image
from other_functionalities.other_utils import *

@app.route('/classification_on_uploaded', methods=['GET', 'POST'])
def classification_on_uploaded():
    form = ClassificationUploadForm()
    if form.validate_on_submit():
        image = request.files[form.image.name]     # It contains the image sent from the client to the server
        img = Image.open(image)
        new_name = new_file_name("uploaded_image") # Avoids overwriting imagenet_subset images and avoid inserting new images in list (jpg rather than JPEG)
        img.save(get_image_path(new_name))         # Saves the image in the image folder with the first available name in the format uploaded_image+counter
        img.close()
        model_id = form.model.data                 # Retrieves the name of the model selected by the user
        clf_output = classify_image(model_id=model_id,
                                    img_id=new_name) # Employs the classification API, using the uploaded image
        result = dict(data=clf_output)
        return render_template('classification_output_up.html',
                               results=result, image_id=new_name)
    return render_template('classification_on_uploaded_select.html',
                           form=form)
