import os.path
import utils
import ppt
import data
from uuid import uuid4

def helper_fn():
    """
    """
    pass

def generate_ppt(project_dir:str, manual_data:dict, root_path:str, project_name:str, timestamp:str, schema):
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

    # NOTE: Not doing anything with parsed_data yet
    parsed_data = parse_data(project_dir, manual_data)
    
    ppt_path = ppt.populate_powerpoint(parsed_data, project_dir, root_path, project_name, None)
    
    schema = schema
    print("")
    print(manual_data)
    print("")

    tadaabject  = {
        "audits_id": audits_id,
        "client_id": client_id,
        "client_name": project_name,
        "domain": domain,
        "ts": timestamp,
        "project_type": project_type,
        "ppt_url": ppt_path,
    }
    # data = None
    
    # ppt._populate_powerpoint(schema, data)

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
        #print(key)
        pass

    return final_data_obj