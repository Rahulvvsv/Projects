import React, { useState } from 'react';

import './ExpenseForm.css';

const ExpenseForm = (props) => {
  const [enteredTitle, setEnteredTitle] = useState('');
  const [enteredAmount, setEnteredAmount] = useState('');
  const [enteredDate, setEnteredDate] = useState('');

  const titleChangeHandler = (event) => {
    setEnteredTitle(event.target.value);
  };

  const amountChangeHandler = (event) => {
    setEnteredAmount(event.target.value);
  };

  const dateChangeHandler = (event) => {
    setEnteredDate(event.target.value);
  };

  const submitHandler = (event) => {
    event.preventDefault();

    const expenseData = {
      title: enteredTitle,
      amount: enteredAmount,
      date: new Date(enteredDate),
    };
    console.log(expenseData);
    props.onSaveExpenseData(expenseData);
    setEnteredTitle('');
    setEnteredAmount('');
    setEnteredDate('');
  };
  const [addState,SetAddState] = useState(0)
  const addStateChanger = () => {
    SetAddState(1);
  }
  const formRemover = () => {
    SetAddState(0);
    setEnteredTitle('');
    setEnteredAmount('');
    setEnteredDate('');
  }
  let addBus =
    <form>
      <div className='new-expense__actions1'>
        <button type='submit' onClick={addStateChanger}>Add Expense</button>
      </div>
    </form>
  if (addState ) {
    addBus =
      <form onSubmit={submitHandler}>
        <div className='new-expense__controls'>
          <div className='new-expense__control'>
            <label>Title</label>
            <input
              type='text'
              value={enteredTitle}
              onChange={titleChangeHandler}
            />
          </div>
          <div className='new-expense__control'>
            <label>Amount</label>
            <input
              type='number'
              min='0.01'
              step='0.01'
              value={enteredAmount}
              onChange={amountChangeHandler}
            />
          </div>
          <div className='new-expense__control'>
            <label>Date</label>
            <input
              type='date'
              min='2019-01-01'
              max='2022-12-31'
              value={enteredDate}
              onChange={dateChangeHandler}
            />
          </div>
        </div>
        <div className='new-expense__actions2'>
        <div className='new-expense__actions'>
          <button type="button" onClick={formRemover} >Cancel</button>
        </div>
        <div className='new-expense__actions'>
          <button type='submit'>Add Expense</button>
        </div>
        </div>

      </form>
  }
  return (
    <div>
    {addBus}
    </div>
  );
};

export default ExpenseForm;
