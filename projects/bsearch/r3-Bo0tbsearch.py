''' Team r3-Bo0t 
	Barry Harris
	Errol Grannum
	Boluwatife Aiki-Raji
	Hallie Lomax
	Brittany Miller
	Eric Walker '''


search_list = [23, 43, 45, 56, 67, 78,89,90]
list_element = 23

def bsearch(search_list):
    size=len(search_list)-1
    middle_point = size/2
    list_len=len(search_list)
    while size>0:
            if list_element == search_list[middle_point]:
                return middle_point
            elif list_element < search_list[middle_point]:
                middle_point = middle_point/2
                size-=1
            else:
                middle_point =(middle_point + list_len)/2
                size-=1
    return "-1"
                

print bsearch(search_list)

#Brittany Miller's bsearch
