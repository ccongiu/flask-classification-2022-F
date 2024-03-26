from flask import render_template

from app import app
from app.forms.histogram_form import HistogramForm
from other_functionalities.histogram_utils import image_histogram
@app.route('/histograms', methods=['GET', 'POST'])
def histograms():
    form = HistogramForm() # Retrieves data from the histogram form

    if form.validate_on_submit():                 # If issued data is valid...
        image_id = form.image.data                # ... retrieves the selected image ...
        output = image_histogram(img_id=image_id) # ... generates the corresponding histogram file ...
        result = dict(data=output)                # ... converts this information into a dictionary (for allowing the same management in the html code as the management employed in the classification)
        return render_template('histogram_output.html', # ... and finally renders the html page related to the output
                               results=result, image_id=image_id)

    # Otherwise, it renders the selection page
    return render_template('histogram_select.html',
                           form=form)