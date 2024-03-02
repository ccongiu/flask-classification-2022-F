from flask import render_template

from app import app
from app.forms.classification_form import ClassificationForm
from ml.classification_utils import classify_image
@app.route('/classifications', methods=['GET', 'POST'])
def classifications():
    form = ClassificationForm()
    if form.validate_on_submit():
        image_id = form.image.data
        model_id = form.model.data
        clf_output = classify_image(model_id=model_id,
                                    img_id=image_id)
        result = dict(data=clf_output)
        return render_template('classification_output.html',
                               results=result, image_id=image_id)
    return render_template('classification_select.html',
                           form=form)
