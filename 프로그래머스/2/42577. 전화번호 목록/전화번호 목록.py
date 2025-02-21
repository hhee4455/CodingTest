def solution(phone_book):
    phone_dict = {phone: True for phone in phone_book}
    for phone in phone_book:
        temp = ""
        for char in phone[:-1]:
            temp += char
            if temp in phone_dict:
                return False

    return True  