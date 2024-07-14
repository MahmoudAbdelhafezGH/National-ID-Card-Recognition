import cv2
import pandas as pd
from preprocessing import preprocess
from featuresExtraction import extractFeatures
from utils import utils
from models import model

def main():
    # Load the input image 
    image = cv2.imread('../data/raw/ausweis_deutsch.jpg') 
    # Preprocessing the data. Convert to gray and apply bilateral filter
    gray_image = preprocess.convert_to_gray(image)
    blurred = preprocess.filter_image(gray_image)

    # Extract edges
    edged = extractFeatures.detect_edges(blurred)

    # find contours and get the one of the max size
    refCnts, hierarchy = extractFeatures.find_contours(edged)
    max_cnt_size, max_cnt_size_index = utils.get_max_size_cnt(refCnts)

    # separate the id card contour from the image for processing
    roi = extractFeatures.extract_card_roi(edged, refCnts , max_cnt_size_index)

    # Extract the ROIs of each field
    firstname_roi = extractFeatures.extract_firstname_roi(roi)
    lastname_roi = extractFeatures.extract_lastname_roi(roi)
    birthday_roi = extractFeatures.extract_birthday_roi(roi)
    nationality_roi = extractFeatures.extract_nationality_roi(roi)
    city_roi = extractFeatures.extract_city_roi(roi)
    expired_roi = extractFeatures.extract_expiration_date_roi(roi)

    # extract the data from the id card
    firstname, lastname, birthday, city, expiration_date, nationality = model.extract_id_data(
        firstname_roi, lastname_roi, birthday_roi, city_roi, expired_roi, nationality_roi
    )
    print(f"First name: {firstname}, Last name: {lastname}, Birthday: {birthday}, City: {city}, Expiration Date: {expiration_date}, Nationality: {nationality}")

    info = {
        'firstname': [firstname],
        'lastname': [lastname],
        'birthday': [birthday],
        'city': [city],
        'nationality': [nationality],
        'expiration date': [expiration_date]
    }
    
    # save the data in a dataframe
    df = pd.DataFrame(info)
    print(df)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()