"""Making sure functions are correct"""
__author__ ="730572910"

def invert (invert_values: dict[str:str]) -> dict[str:str]:
    """Invert the keys and values in the dictionary"""
    inverted_dict = {}
    for key in invert_values:
        values = invert_values[key]
        if values in inverted_dict:
            raise KeyError("duplicate key value found")
        else:
            inverted_dict[values]= key
    return inverted_dict
    
        

def count (listed_values: list[str]) -> dict[str:int]:
    """Count the times a string occurs in the list."""
    count_dict : dict[str:int] = {}
    for item in listed_values:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def favorite_color (fav_colors: dict[str:str]) -> str:
    """finding the most common favorite color"""
    color_list: list[str] =[]
    for names in fav_colors:
        color_list.append(fav_colors[names])
    color_dict: dict[str:int] = count(color_list)

    fav_color: str = ""
    tally: int = 0
    for colors in color_dict:
        if color_dict[colors] > tally:
            fav_color = colors
            tally = color_dict[colors]
            return fav_color
    
        

def bin_len(words: list[str]) -> dict[int, set[str]]:
    """counting and organizing the length of words"""
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = set()
        result[length].add(word)
    return result
        
    
        