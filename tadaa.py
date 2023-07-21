import os.path
import utils
import ppt
import data




'''
Current API Endpoints

* ppt.populate_powerpoint
    INPUT
        * Annotated Template
        * Data
    OUTPUT
        * Completed PPT

* tadaa.parse_data

* tadaa.generate_audit

* utils.match_target_hint_files

* utils.get_abs_path

* utils.get_data_obj

'''

'''
New API Endpoints

* tadaa.generate_audit

    * parse xls files
    * create tadaabject
    * create powerpoint
    * save to db
    * send to client

* tadaa.request_audits(client_name) -> all_audits
* tadaa.request_audit(audit_id) -> audit_data


tableParser class
    handles csv/xls parsing from Sitebulb exports
tadaabjectCreation class
    takes data from webAPI and tableParser classes and organizes into tadaabject



'''

def __generate_audit(project_dir, manual_data, root_path):
    """

    @param

    @return tadaabject: Our custom tech audit data object
    """
    tadaabject  = {
        "audits_id": "audits_id",
        "client_id": "client_id",
        "client_name": "project_name",
        "domain": "domain",
        "ts": "timestamp",
        "project_type": "project_type",
        "ppt_url": "pop_ppt",
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