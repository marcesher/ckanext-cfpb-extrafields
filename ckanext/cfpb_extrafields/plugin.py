import ckan.plugins as p
import ckan.plugins.toolkit as tk
import pprint


import validators as v


class ExampleIDatasetFormPlugin(p.SingletonPlugin, tk.DefaultDatasetForm):
    p.implements(p.IDatasetForm)
    p.implements(p.IConfigurer)
    # p.implements(p.ITemplateHelpers)


    # def get_helpers(self):
    # return {'type_of_entries': ['Consumers', 'Financial Institutions', 'Employees', 'Government', 'Other'],
    #             'sensitivity_levels': [{'value': 'Public'}, {'value': 'Low'}, {'value': 'Medium'}, {'value': 'High'}]}

    def _modify_package_schema(self, schema):
        schema.update({
            'sensitivity_level': [tk.get_validator('ignore_missing'),
                                  tk.get_converter('convert_to_extras')],
            'has_pii': [tk.get_validator('ignore_missing'),
                        tk.get_converter('convert_to_extras')],
            'type_of_entries': [tk.get_validator('ignore_missing'),
                                tk.get_converter('convert_to_extras')],
            'pra_control_num': [tk.get_validator('ignore_missing'),
                                v.pra_control_num_validator,
                                tk.get_converter('convert_to_extras')],
            'size_in_mb': [tk.get_validator('ignore_missing'),
                           v.positive_number_validator,
                           tk.get_converter('convert_to_extras')],
            'time_period_start_date': [tk.get_validator('ignore_missing'),
                                       tk.get_converter('convert_to_extras')],
            'pia_url': [tk.get_validator('ignore_missing'),
                        tk.get_converter('convert_to_extras')],
            'storage_location': [tk.get_validator('ignore_missing'),
                                 tk.get_converter('convert_to_extras')],
        })
        # pprint.pprint(schema)
        return schema

    def create_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).show_package_schema()
        schema.update({
            'sensitivity_level': [tk.get_converter('convert_from_extras'),
                                  tk.get_validator('ignore_missing')],
            'has_pii': [tk.get_converter('convert_from_extras'),
                        tk.get_validator('ignore_missing')],
            'type_of_entries': [tk.get_converter('convert_from_extras'),
                                tk.get_validator('ignore_missing')],
            'pra_control_num': [tk.get_converter('convert_from_extras'),
                                v.pra_control_num_validator,
                                tk.get_validator('ignore_missing')],
            'size_in_mb': [tk.get_converter('convert_from_extras'),
                           v.positive_number_validator,
                           tk.get_validator('ignore_missing')],
            'time_period_start_date': [tk.get_converter('convert_from_extras'),
                                       tk.get_validator('ignore_missing')],
            'pia_url': [tk.get_converter('convert_from_extras'),
                        tk.get_validator('ignore_missing')],
            'storage_location': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
        })
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')
