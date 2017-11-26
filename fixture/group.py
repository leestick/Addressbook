__author__ = 'ioK'


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, name, header, footer):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        wd.find_element_by_name("submit").click()
        self.open_groups_page()

    def select_first_group(self, wd):
        wd.find_element_by_name("selected[]").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_groups_page()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form

        # submit modification
        wd.find_element_by_name("update").click()
        self.open_groups_page()


