from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    url_for,
    current_app,
    abort,
)
from werkzeug.utils import secure_filename
import os
import imghdr
from .s3 import create_bucket, s3_resource, s3_client, enable_bucket_versioning

# print(
#     create_bucket(
#         bucket_prefix="studywithpam-articles", s3_connection=s3_resource.meta.client
#     )
# )

BUCKET_NAME = "studywithpam-articles67e4cdac-4d89-4e95-80fd-ba3f18e28532"
enable_bucket_versioning(BUCKET_NAME)

upload_image_blueprint = Blueprint("upload_image_blueprint", __name__)


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return "." + (format if format != "jpeg" else "jpg")


@upload_image_blueprint.route(
    "/admin/admin-dashboard/upload-image", methods=["GET", "POST"]
)
def upload_image():
    if request.method == "POST":
        file = request.files["file"]
        filename = secure_filename(file.filename)
        if filename != "":
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in current_app.config[
                "UPLOAD_EXTENSIONS"
            ] or file_ext != validate_image(file.stream):
                abort(400)
            file.save(
                os.path.join(current_app.config["UPLOAD_PATH"], filename)
            )
            # UPLOAD TO AWS S3
            print(file)
            s3_client.upload_fileobj(
                file,
                BUCKET_NAME,
                filename,
                ExtraArgs={
                    "ACL": "public-read",
                    "ContentType": file.content_type,
                },
            )
        # s3.upload_fileobj(
        #     file,
        #     os.getenv("AWS_BUCKET_NAME"),
        #     file.filename,
        #     ExtraArgs={
        #         "ACL": acl,
        #         "ContentType": file.content_type
        #     }
        # )
        return redirect(url_for("upload_image_blueprint.upload_image"))
    return render_template("upload-image.html")
