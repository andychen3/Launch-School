def find_list_by_id(list_id, lists):
    return next((lst for lst in lists if lst['id'] == list_id), None)

lst = find_list_by_id(list_id, session['lists'])

def find_todo_by_id(todo_id, todos):
    return next((todo for todo in todos if todo["id"] == todo_id), None)

todo = find_todo_by_id(todo_id, lst["todos"])