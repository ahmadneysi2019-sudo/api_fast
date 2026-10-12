from fastapi_offline import FastAPIOffline
app = FastAPIOffline()
mylist = [100,200,300,200]

@app.get('/')
def say_hello():
    return{'hello':'world'}


@app.get('/getitems/')
def get_items():
    return {'output':mylist}


@app.get('/lastitem/')
def get_lastitem():
    if len(mylist) > 0 :
        return {'output':mylist[-1]}
    else:
        return {'list is empty'}



@app.get('/firstitem/')
def get_lastitem():
    if len(mylist) > 0 :
        return {'output':mylist[0]}
    else:
        return {'list is empty'}
    
@app.post('/additem/{new_item}')
def insert_item(new_item:int):
     mylist.append(new_item)
     return {'new output':mylist}


@app.delete('/removeitem/')
def remove_item(item:int):
    if item in mylist:
        mylist.remove(item)
        return {'list after remove':mylist}
    else:
        return{f'{item}not found in list'}
    
@app.delete('/popindex')
def pop_item(index:int):
    if index >= 0 and index < len(mylist):
        r = mylist.pop(index)
        return{f'{r}deleted from list'}
    else:
        return{'index is wrong'}


@app.put('/updateitem/')
def update_item(index:int,new_item:int):
    if index >= 0 and index < len(mylist):
        mylist[index]= new_item
        return{'update list':mylist}
    else:
        return{f'index of {index},not found'}

@app.put('/updateolditem/')
def update_old_item(old_item:int,new_item:int):
    if old_item in mylist:
        i = mylist.index(old_item)
        mylist[i]= new_item
        return{'list update':mylist}
    else:
        return{f'{old_item}not found'}

    