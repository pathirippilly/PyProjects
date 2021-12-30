from typing import Union,List
from common.custom_exceptions import InvalidInputArgumentType
def beautify_str(inp_item: Union[str,List]) -> Union[str,List]:
    """
    Description:removes following characters from string or list of strings--> white spaces,\r,\n

    :param inp_item : string to be passed
    :type inp_item : str or list
    :rtype : str or list

    """
    if isinstance(inp_item,str):
        return inp_item.replace(" ", "").replace("\n", "").replace("\r", "")
    elif isinstance(inp_item,list):
        return [item.replace(" ", "").replace("\n", "").replace("\r", "") for item in inp_item]
    else
        raise InvalidInputArgumentType({'inp_item':'str'})