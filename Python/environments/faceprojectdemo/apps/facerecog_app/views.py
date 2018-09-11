from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
import cv2
import sys
import imutils
import math
import base64
import json
import requests

def newuser(request): 
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
            errors=messages.json(errors)
        return requests.post('localhost:4200/', errors)
    else:
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = password)
        request.session['user_id'] = User.objects.get(email = request.POST['email']).id
        with open("face.jpeg", "wb") as fh:
            fh.write(base64.b64decode(newdata['img_data']))
        image = cv2.imread("face.jpeg")
        image = imutils.resize(image, width=600)

        # Create the haar cascade
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
        eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')

        # Read the image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.5,
            minNeighbors=5,
            minSize=(20, 20),
            maxSize = (400, 400)
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            print('FACE',x, "left",y, "top",x+w, "right",y+h,"bottom",w,h)
            fwid=w
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = image[y:y+h, x:x+w]
            eyes = eyeCascade.detectMultiScale(
                roi_gray,
                scaleFactor=1.01,
                minNeighbors=5,
                minSize=(48, 48),
                maxSize=(65, 65)
            )
            hairline = 0
            ebot = 0
            eyewid = []
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
                print('EYE', "left", ex, "top", ey, "right", ex+ew,"bottom", ey+eh, "width", ew, "height", eh)
                hairline = hairline+ey+eh/2
                ebot = ebot + (ey+eh)/2
                eyewid = eyewid+[ex]
                eyewid = eyewid+[ex+ew]
            smiles = smileCascade.detectMultiScale(
                roi_gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(50, 120),
                maxSize=(100, 220)
            )
            for (ex,ey,ew,eh) in smiles:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
                mwid=ew
                mtop=ey
                mbot=ey+eh
                mleft = ex
                mright = ex+ew
                print('MOUTH', "left", ex, "top", ey, "right", ex+ew, "bottom", ey+eh, "width", ew ,"height", eh)

        #validation
        errors = {}
        if len(faces) > 1:
            errors["faces"] = "Multiple faces detected please take another picture"
        if len(faces) < 1:
            errors["faces"] = "No faces detected please take another picture"
        if len(eyes) > 2:
            errors["eyes"] = "More than 2 eyes detected please take another picture"
        if len(eyes) < 2:
            errors["eyes"] = "Less than 2 eyes detected please take another picture"
        if len(smiles) > 1:
            errors["smiles"] = "Multiple mouths detected please take another picture"
        if len(smiles) < 1:
            errors["smiles"] = "No mouths detected please take another picture"
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
                errors=messages.json(errors)
            return requests.post('localhost:4200/', errors)
        else:
            #calculations
            mofa = mwid/fwid
            chinheight = fwid-mbot
            hairline = hairline/2
            hairtomouth1 = math.atan((mleft-eyewid[0])/(mbot-hairline))*180/math.pi
            hairtomouth2 = math.atan((eyewid[3]-mright)/(mbot-hairline))*180/math.pi
            chinhypo = (chinheight**2+(mwid/2)**2)**0.5
            chinangle = 180 - 2*math.asin(chinheight/chinhypo)*180/math.pi
            hairangle = (hairtomouth1+hairtomouth2)/2

            #shape classifier
            if (hairangle>16 or hairangle<-16):
                if (chinangle<108):
                    shape = 'heart'
                else:
                    shape = 'round'
            if (hairangle<=16 and hairangle>=-16):
                if (chinangle<108):
                    shape = 'diamond'
                else:
                    if(mofa<0.4):
                        shape = 'oval'
                    else:
                        shape = 'square'

            image = cv2.imwrite('face.jpeg',image)

            #create new face object in databasee
            Face.objects.create(chin_angle = chinangle, mofa_ratio = mofa, hlmo_angle = hairangle, shape = shape, user = User.objects.get(id = user_id))
            
            #context objects to kickback
            with open(image, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())   
            context_before = {
                'shape': shape,
                'image': encoded_string
            }
            context = context_before.json(context)
            return requests.post('http:local:4200/', context)




def demo(request): 
    with open("face.jpeg", "wb") as fh:
        fh.write(base64.b64decode(request.POST['img_data']))
    image = cv2.imread("face.jpeg")
    image = imutils.resize(image, width=600)

     # Create the haar cascade
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')

    # Read the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(20, 20),
        maxSize = (400, 400)
    )


    print("Found {0} faces!".format(len(faces)), faces)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        print('FACE',x, "left",y, "top",x+w, "right",y+h,"bottom",w,h)
        fwid=w
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        eyes = eyeCascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.01,
            minNeighbors=5,
            minSize=(48, 48),
            maxSize=(65, 65)
        )
        hairline = 0
        ebot = 0
        eyewid = []
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
            print('EYE', "left", ex, "top", ey, "right", ex+ew,"bottom", ey+eh, "width", ew, "height", eh)
            hairline = hairline+ey+eh/2
            ebot = ebot + (ey+eh)/2
            eyewid = eyewid+[ex]
            eyewid = eyewid+[ex+ew]
        smiles = smileCascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(50, 130),
            maxSize=(100, 200)
        )
        for (ex,ey,ew,eh) in smiles:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
            mwid=ew
            mtop=ey
            mbot=ey+eh
            mleft = ex
            mright = ex+ew
            print('MOUTH', "left", ex, "top", ey, "right", ex+ew, "bottom", ey+eh, "width", ew ,"height", eh)
        errors = {}
        if len(faces) > 1:
            errors["faces"] = "Multiple faces detected please take another picture"
        if len(faces) < 1:
            errors["faces"] = "No faces detected please take another picture"
        if len(eyes) > 2:
            errors["eyes"] = "More than 2 eyes detected please take another picture"
        if len(eyes) < 2:
            errors["eyes"] = "Less than 2 eyes detected please take another picture"
        if len(smiles) > 1:
            errors["smiles"] = "Multiple mouths detected please take another picture"
        if len(smiles) < 1:
            errors["smiles"] = "No mouths detected please take another picture"
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
                errors=messages.json(errors)

            image = cv2.imwrite('face.jpeg',image)

            #context objects to kickback
            with open(image, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())   
            context_before = {
                    'error': errors,
                    'image': encoded_string
                }
            context = context_before.json(context)
            return requests.post('http:local:4200/', context)
        else:
            #calculations
            mofa = mwid/fwid
            chinheight = fwid-mbot
            hairline = hairline/2
            hairtomouth1 = math.atan((mleft-eyewid[0])/(mbot-hairline))*180/math.pi
            hairtomouth2 = math.atan((eyewid[3]-mright)/(mbot-hairline))*180/math.pi
            chinhypo = (chinheight**2+(mwid/2)**2)**0.5
            chinangle = 180 - 2*math.asin(chinheight/chinhypo)*180/math.pi
            hairangle = (hairtomouth1+hairtomouth2)/2
            print(mofa, chinangle, hairangle,eyewid)

            #shape classifier
            if (hairangle>16 or hairangle<-16):
                if (chinangle<108):
                    shape = 'heart'
                else:
                    shape = 'round'
            if (hairangle<=16 and hairangle>=-16):
                if (chinangle<108):
                    shape = 'diamond'
                else:
                    if(mofa<0.4):
                        shape = 'oval'
                    else:
                        shape = 'square'

            image = cv2.imwrite('face.jpeg',image)

            #context objects to kickback
            with open(image, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())   
            context_before = {
                    'shape': shape,
                    'image': encoded_string
                }
            context = context_before.json(context)
            return requests.post('http:local:4200/', context)



def login(request): 
    pass
    # r= requests.get(f'')
    # logindata = r.json()
    # errors = User.objects.login_validator(logindata)
    # if len(errors):
    #     for key, value in errors.items():
    #         messages.error(request, value)
    #     return requests.get('localhost:4200/', errors)
    # else:
    #     request.session['user_id'] = User.objects.get(email = logindata['email']).id
    #     context_before = {
    #             'shapes': Face.objects.filter(user = User.objects.get(id = user_id)).shape,
    #         }
    #     context = context_before.json(context)
    #     return requests.get('http:local:4200/', context)
