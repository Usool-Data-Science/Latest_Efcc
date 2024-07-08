

#!/usr/bin/python3
def calculate_completion_percentage(dicts_list):
    """
    Calculate the completion percentage of a list of dictionaries.

    Args:
    dicts_list (list): A list of dictionaries to be checked for completeness.

    Returns:
    float: The completion percentage of the dictionaries in the list.
    """
    if not dicts_list:
        return 0.0

    total_dicts = len(dicts_list)
    completed_dicts = 0

    for d in dicts_list:
        if all(d.values()):
            completed_dicts += 1

    completion_percentage = (completed_dicts / total_dicts) * 100
    return completion_percentage


# def progress(obj):
#     """Checks the progress of obj"""
#     prog = 0
#     size = len(obj)

#     for v in obj.values():
#         if v:
#             prog += 1
#     result = int((prog/size) * 100)

#     return result

# check it out later

# if all([progress(dic) == 100 for dic in complainants_dict]):
#     comp_progress = 100
# else:
#     incomplete = list(filter(lambda x: progress(x) != 100, complainants_dict))
#     complete = list(filter(lambda x: progress(x) == 100, complainants_dict))
#     if len(incomplete) == 1:
#         all_progress = len(complete)/len(complainants_dict)*100
#         incomplete_progress = progress(incomplete[0])*100
#         comp_progress = all_progress + incomplete_progress
#     else:
#         comp_progress = complete/len(complainants_dict)

