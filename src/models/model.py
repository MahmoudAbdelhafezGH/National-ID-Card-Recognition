import pytesseract
def extract_id_data(firstname_roi, lastname_roi, birthday_roi, city_roi, expired_roi, nationality_roi):
    firstname = pytesseract.image_to_string(firstname_roi, lang='deu', config='--psm 6').strip()
    lastname = pytesseract.image_to_string(lastname_roi, lang='deu', config='--psm 6').strip()
    birthday = pytesseract.image_to_string(birthday_roi, lang='deu', config='--psm 6').strip()
    city = pytesseract.image_to_string(city_roi, lang='deu', config='--psm 6').strip()
    expiration_date = pytesseract.image_to_string(expired_roi, lang='deu', config='--psm 6').strip()
    nationality = pytesseract.image_to_string(nationality_roi, lang='deu', config='--psm 6').strip()
    return firstname, lastname, birthday, city, expiration_date, nationality