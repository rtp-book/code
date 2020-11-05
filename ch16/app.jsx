<form onSubmit={handleSubmit}>
    <label htmlFor="newItem">
        {len(editItem) === 0 ? "Add Item: " : "Edit Item: "}
    </label>
    <input id="newItem" onChange={handleChange} value={newItem}/>
    <input type="submit"/>
    <ol>
        <ListItems
            listItems={listItems}
            handleDelete={handleDelete}
            handleEdit={handleEdit}
        />
    </ol>
</form>

