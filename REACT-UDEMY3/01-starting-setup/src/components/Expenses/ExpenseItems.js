import { useState } from 'react';
import './ExpenseItems.css';
import ExpenseDate from "./ExpenseDate";
import Card from '../UI/Card'
function ExpenseItem(props) {
    const [title, setTitle] = useState(props.title);

    const expenseAmount = props.amount;
    // Instead of assigning props to constants you can directly use them in divs
    const clickHandler = () => {
        setTitle("Updated!");
        console.log("Clicked!!");
        console.log(title);
    }
    return (

        <Card className="expense-item ">
            <ExpenseDate fdate={props.date}></ExpenseDate>
            <div className="expense-item__description ">
                <h2>{title}</h2>
                <div className="expense-item__price">{expenseAmount}</div>
                <button onClick={clickHandler} >HI there</button>
            </div>
        </Card>
    );

}
export default ExpenseItem;