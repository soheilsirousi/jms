

def generate_response(success: bool, content= None, error= None):
    data = {}
    if success:
        data['success'] = True
        data['content'] = content
        data['error'] = None
    else:
        data['success'] = False
        data['content'] = None
        data['error'] = error

    return data