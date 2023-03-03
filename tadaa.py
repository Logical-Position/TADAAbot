import os.path
import utils
import ppt
import data

def parse_data(project_dir):
    """
    Takes the upload directory and organizes the data necessary for the tech audit. Returns our custom data object.

    @param [str] upload_dir: path to the server's upload directory.

    @return [dict] final_data_obj: our custom data object {target_file: [data]} that contains Pandas dataframe/series objects.
    """

    all_uploaded_files = os.listdir(project_dir)

    matched_list = utils.match_target_hint_files(all_uploaded_files)
    matched_paths = utils.get_abs_paths(matched_list, project_dir)

    final_data_obj = utils.get_data_obj(matched_paths)
    
    for key in final_data_obj.keys():
        print(key)

    return final_data_obj


def generate_audit(final_data_obj, project_dir, root_path, project_name):
    """
    Generates a populated Powerpoint document using the custom data object.

    @param [dict] final_data_obj: our custom data object {target_file: [data]} that contains Pandas dataframe/series objects.
    @param [str] root_path: path to the server's root directory.

    @return [list] pop_ppt: a Powerpoint doc populated with values calculated using the custom data object.
    """
    pop_ppt = ppt.populate_powerpoint(final_data_obj, project_dir, root_path, project_name)
    
    return pop_ppt


def data_vis():
    data.visualize()