class Factory:
    @staticmethod
    def get_positions_from_line_sep_component_sep(str_path:str, line_sep:str, component_sep:str)->List[Position]:
        scenario_configs_dict = Mrs.get_scnario_configs()
        file_path = Path()
        file_storage = File(file_path)
        text = file_storage.get_ram()



