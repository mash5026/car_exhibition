from django.core.exceptions import ValidationError

# >-----create choice list for choosing type of agency-----<
OFFICIAL = "official"
OTHER = "other"
LIST_STATUS = [
    ('OFFICIAL',"رسمی"),('OTHER',"متفرقه")
]

# >-----create path for saving image with selfname-----<
def path_car(instance,filename):
    return 'car/images/{}.{}'.format(instance.name, filename.split(".")[-1])

# >-----create validator for check size image-----<
def validat_image(file):
    if (file.size>2097152):
        raise ValidationError("سایز فایل شما می بایست کمتر از 2مگابایت باشد")
