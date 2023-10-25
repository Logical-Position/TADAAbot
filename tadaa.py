import os.path
import utils
import ppt
import data
from uuid import uuid4

# NEW DEF
def _generate_ppt(form_data: dict):
    """
    """
    pass

def __generate_audit(project_dir:str, manual_data:dict, root_path:str, project_name:str, timestamp:str):
    """
    Generates a populated Powerpoint document using the custom data object.
    
    @param project_dir: Project path by timestamp "os.path/uploads/[timestamp]"
    @param manual_data: Data submitted through form fields
    @param root_path: the path to the root of application

    @return [dict] tadaabject: Our custom tech audit data object
    """

    audits_id = str(uuid4())
    client_id = str(uuid4())
    domain = manual_data["domain_url"]
    project_type = "InvalidType"

    # Not doing anything with parsed_data yet
    parsed_data = parse_data(project_dir, manual_data)
    pop_ppt = ppt.populate_powerpoint(parsed_data, project_dir, root_path, project_name, None)

    tadaabject  = {
        "audits_id": audits_id,
        "client_id": client_id,
        "client_name": project_name,
        "domain": domain,
        "ts": timestamp,
        "project_type": project_type,
        "ppt_url": pop_ppt,
    }
    return tadaabject



def parse_data(project_dir, manual_data):
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
    print(" ===== TADAABJECT ===== ")
    print(final_data_obj)
    print(" ===== TADAABJECT ===== ")
    return final_data_obj