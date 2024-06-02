import cv2
import numpy as np

def detect_edges(img, t_lower = 245, t_upper = 250):
    edged = cv2.Canny(img, t_lower, t_upper) 
    return edged

def find_contours(img):
    refCnts, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print("Number of Contours found = " + str(len(refCnts))) 
    return refCnts, hierarchy

def extract_card_roi(img, cnts, max_cnt_size_index):
    x, y, w, h = cv2.boundingRect(cnts[max_cnt_size_index])
    roi = img[y:y + h, x:x + w]
    return roi

def extract_firstname_roi(img):    
    roi_nrows = img.shape[0]
    roi_ncols = img.shape[1]
    firstname_roi = img[roi_nrows//3: 2*roi_nrows//5, 2*roi_ncols//5: 99*roi_ncols//100]
    cv2.imshow('first name roi', firstname_roi)
    return firstname_roi

def extract_lastname_roi(img):
    roi_nrows = img.shape[0]
    roi_ncols = img.shape[1]
    lastname_roi = img[roi_nrows//6: 3*roi_nrows//10, 2*roi_ncols//5: 99*roi_ncols//100]
    cv2.imshow('last name roi', lastname_roi)
    return lastname_roi

def extract_birthday_roi(img):
    roi_nrows = img.shape[0]
    roi_ncols = img.shape[1]
    birthday_roi = img[47*roi_nrows//100: 55*roi_nrows//100, 45*roi_ncols//100: 68*roi_ncols//100]
    kernel = np.ones((3, 3), np.uint8)
    birthday_roi = cv2.morphologyEx(birthday_roi, cv2.MORPH_CLOSE, kernel) 
    cv2.imshow('birthday roi', birthday_roi)
    return birthday_roi

def extract_expiration_date_roi(img):
    roi_nrows = img.shape[0]
    roi_ncols = img.shape[1]
    expired_roi = img[71*roi_nrows//100: 77*roi_nrows//100, 2*roi_ncols//5: 99*roi_ncols//100]
    kernel = np.ones((3, 3), np.uint8)
    expired_roi = cv2.morphologyEx(expired_roi, cv2.MORPH_CLOSE, kernel) 
    cv2.imshow('Expiration date roi', expired_roi)
    cv2.waitKey(0)
    return expired_roi

def extract_city_roi(img):
    roi_nrows = img.shape[0]
    roi_ncols = img.shape[1]
    city_roi = img[58*roi_nrows//100: 64*roi_nrows//100, 2*roi_ncols//5: 99*roi_ncols//100]
    cv2.imshow('City roi', city_roi)
    return city_roi

def extract_nationality_roi(img):
    roi_nrows = img.shape[0]
    roi_ncols = img.shape[1]
    nationality_roi = img[47*roi_nrows//100: 55*roi_nrows//100, 69*roi_ncols//100: 99*roi_ncols//100]
    cv2.imshow('Nationality roi', nationality_roi)
    return nationality_roi


