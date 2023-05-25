# Flask App Classifier

A Python flask app that makes use of a ML cancer classifier model 

### Run App: 

Dependencies : 

- add `model.p` file to `\model\model.p`
- you can download mine from [here](https://drive.google.com/file/d/1si-tpggXbUbMriAsRdTAW4V6PG2T10Ad/view?usp=sharing)

to Install requirments : 

    pip install -r requirements.txt


to run app : 

    python main.py 

### How it works 

- Flask Accepts uploaded images and save it to `/uploads/<filename>`
- On images submission it get passed to `TumorPredictor` and return `result`
- Image is then renamed to start with `result` 

### Next Steps

To achieve better prediction accuracy, 
All what we have to do is to replace the model file with more advanced one.

> If a different ML Library is used in the classification code,<br>
> then we will need to update the `TumorPredictor` class while keeping methods names.

<br>

---

### Troubleshooting 
to fix a bug in `flask_uploades`
Solution obtained from [flask uploads import error](https://stackoverflow.com/questions/61628503/flask-uploads-importerror-cannot-import-name-secure-filename)

1) get library file path:


        import flask_uploads
        print(flask_uploads.__file__)


2) Edit Import lines as follows: 

        # from werkzeug import secure_filename, FileStorage
        from werkzeug.utils import secure_filename
        from werkzeug.datastructures import  FileStorage