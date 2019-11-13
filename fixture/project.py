from model.project import Project
import time


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        # init project creation
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        # fill project form
        self.fill_project_form(project)
        # submit project creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        wd.find_element_by_link_text("Proceed").click()
        self.open_projects_page()
        self.project_cache = None

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("status", project.status)
        self.change_field_value("inherit_global", project.inherit_global)
        self.change_field_value("view_state", project.view_state)
        self.change_field_value("description", project.description)
        self.change_field_value("description", project.description)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.project_cache = []
            table = wd.find_element_by_xpath("//body//table[3]")
            table_rows = table.find_elements_by_tag_name("tr")
            for row in table_rows[2: len(table_rows)]:
                cells = row.find_elements_by_tag_name("td")
                name = cells[0].text
                status = cells[1].text
                inherit_global = cells[2].text
                view_state = cells[3].text
                description = cells[4].text
                self.project_cache.append(Project(name = name, status = status, inherit_global = inherit_global,
                                                  view_state = view_state, description = description))
        return list(self.project_cache)
