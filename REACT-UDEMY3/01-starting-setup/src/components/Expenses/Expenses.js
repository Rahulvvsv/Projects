import React, { useState } from 'react';

import ExpenseItem from './ExpenseItem';
import Card from '../UI/Card';
import ExpensesFilter from './ExpensesFilter';
import './Expenses.css';

const Expenses = (props) => {
  const [filteredYear, setFilteredYear] = useState('0');

  const filterChangeHandler = selectedYear => {
    setFilteredYear(selectedYear);
  };

  const CheckYear = (dates) => {
    console.log(dates.date);
    if (filteredYear === '0') {
      return dates
    }
    else {
      return dates.date.getFullYear().toString() === filteredYear;
    }
  }
  const listed = props.expen.filter(CheckYear);
  let expensesContent = <p>No Expenses Found in this year</p>;
  if (listed.length > 0) {

    expensesContent = listed.map(expens =>
      <ExpenseItem
        key={expens.id}
        title={expens.title}
        amount={expens.amount}
        date={expens.date}
      ></ExpenseItem>


    )
  }


return (
  <div>
    <Card className='expenses'>
      <ExpensesFilter selected={filteredYear} onChangeFilter={filterChangeHandler} />
    {expensesContent}

    </Card>
  </div>
);
};

export default Expenses;
