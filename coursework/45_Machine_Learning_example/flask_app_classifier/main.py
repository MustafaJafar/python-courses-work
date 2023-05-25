import os
from PIL import Image
from wtforms import SubmitField 
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed 
from flask import Flask, render_template, send_from_directory
from flask_uploads import UploadSet, IMAGES, configure_uploads, url_for


from  predictor import TumorPredictor


app = Flask(__name__)
app.config["SECRET_KEY"] = "asddfg"
app.config["UPLOADED_PHOTOS_DEST"] = os.path.join(os.getcwd(), "uploads")

IMAGES += ("tiff",) # add tiff to the allowed extentions 

photos = UploadSet("photos" , IMAGES)
configure_uploads(app, photos)

class UploadForm(FlaskForm):
    photo = FileField(
        validators = [
                FileAllowed(photos, "Only Images are allowed"),
                FileRequired("File field should not be empty") ] )

    submit = SubmitField("Upload")


def rename_image(image_path , prediction_test): 
    file_name = os.path.basename(image_path)
    dir_name =  os.path.dirname(image_path)
    new_name = f"{prediction_test}_{file_name}"

    new_image_path = os.path.join(dir_name , new_name)
    os.rename(image_path, new_image_path)


    return "/" + new_image_path

def convert_tiff_to_png(image_path):

    if (image_path.endswith(".tiff")):
        image = Image.open(image_path)
        
        png_image_path = image_path.replace(".tiff", ".png")
        image.save(png_image_path)
        
        os.remove(image_path)

        return "/" + png_image_path
    
    return "/" + image_path

@app.route("/uploads/<filename>")
def get_file(filename): 
    return send_from_directory(app.config["UPLOADED_PHOTOS_DEST"] , filename)
 


@app.route("/", methods= ["GET", "POST"])
def upload_image():
    form = UploadForm()
    if form.validate_on_submit() : 
        filename = photos.save(form.photo.data)
        file_url = url_for("get_file" , filename=filename)

        image_path = os.path.join(os.getcwd(),file_url[1:])
        result = TumorPredictor().predict(image_path)
        
        file_url = convert_tiff_to_png(file_url[1:]) # convert tiff to png as flask doesn't support displaying tiff
        file_url = rename_image(file_url[1:], result)

    else : 
        file_url = None
        result=""

    return render_template("index.html", form=form, file_url=file_url , prediction_result = result)

if __name__ == "__main__" : 
    app.run()