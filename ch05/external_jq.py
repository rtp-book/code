# __pragma__ ('alias', 'jq', '$')

def set_click():
    def add_item():
        jq("ol").append("<li>List item</li>")

    jq("#append_btn").click(add_item)

def doc_ready():
    jq(document).ready(set_click)

