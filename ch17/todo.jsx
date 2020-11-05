import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      newTask: "",
      editTask: null,
      taskList: Array(),
      taskCount: 0,
      taskFilter: "all"
    };
  }

  handleSubmit = (event) => {
    event.preventDefault();
    const taskList = this.state.taskList.slice();
    if (this.state.editTask) {
      const taskIndex = taskList.findIndex(
        (task => task.name === this.state.editTask.name)
      );
      taskList[taskIndex].name = this.state.newTask;
    } else {
      taskList.push({name: this.state.newTask, status: false});
    }
    this.setState({newTask: "", editTask: null, taskList: taskList});
  }


  handleEdit = (task) => {
    this.setState({newTask: task.name, editTask: task});
  }

  handleDelete = (task) => {
    const taskList = this.state.taskList.filter(function (item) {
      return item.name !== task.name;
    });
    this.setState({taskList: taskList});
  }

  handleChange = (event) => {
    if (event.target.name === "taskFilter") {
      this.setState({taskFilter: event.target.value});
    } else {
      this.setState({newTask: event.target.value});
    }
  }

  handleChangeStatus = (event, task) => {
    const taskList = this.state.taskList.slice();
    const taskIndex = taskList.findIndex((item => item.name === task.name));
    taskList[taskIndex].status = event.target.checked;
    this.setState({taskList: taskList});
  }

  renderTask = (task) => {
    const taskFilter = this.state.taskFilter
    if (taskFilter === "all" ||
        (taskFilter === "open" && !task.status) ||
        (taskFilter === "closed" && task.status)
    ) {
      return (
          <li key={task.name}>{task.name}
            <button
                type="button"
                onClick={() => this.handleDelete(task)}
            >Delete
            </button>
            <button
                type="button"
                onClick={() => this.handleEdit(task)}
            >Edit
            </button>
            <label htmlFor="status"> Completed:</label>
            <input type="checkbox"
                   id="status"
                   onChange={(event) => this.handleChangeStatus(event, task)}
                   checked={task.status}
            />
          </li>
      );
    } else {
      return null
    }

  }

  updateCount() {
    let taskList
    switch (this.state.taskFilter) {
      case "open":
        taskList = this.state.taskList.filter((task => !task.status));
        break;
      case "closed":
        taskList = this.state.taskList.filter((task => task.status));
        break;
      default:
        taskList = this.state.taskList.slice();
    }

    const taskCount = taskList.length;
    this.setState({taskCount: taskCount})
  }

  componentDidMount() {
    document.title = "ToDo List";
  }

  componentDidUpdate(prevProps, prevState) {
    if (prevState.taskList !== this.state.taskList ||
        prevState.taskFilter !== this.state.taskFilter
    ) {
      this.updateCount();
    }
  }

  render() {
    const taskFilter = this.state.taskFilter;
    return (
        <form onSubmit={this.handleSubmit}>
          <div>Number of Tasks: {this.state.taskCount}</div>
          <div>
            <label htmlFor="all">All Tasks:</label>
            <input type="radio"
                   name="taskFilter"
                   id="all"
                   value="all"
                   onChange={this.handleChange}
                   checked={taskFilter === "all"}
            />
            <label htmlFor="open"> Active:</label>
            <input type="radio"
                   name="taskFilter"
                   id="open"
                   value="open"
                   onChange={this.handleChange}
                   checked={taskFilter === "open"}
            />
            <label htmlFor="closed"> Completed:</label>
            <input type="radio"
                   name="taskFilter"
                   id="closed"
                   value="closed"
                   onChange={this.handleChange}
                   checked={taskFilter === "closed"}
            />
          </div>
          <label htmlFor="newTask">
            {this.state.editTask ? "Edit Task: " : "Add Task: "}
          </label>
          <input id="newTask"
                 onChange={this.handleChange}
                 value={this.state.newTask}
          />
          <input type="submit"/>
          <ol>
            {this.state.taskList.map(this.renderTask)}
          </ol>
        </form>
    );
  }
}

ReactDOM.render(<App/>, document.getElementById('root'));

