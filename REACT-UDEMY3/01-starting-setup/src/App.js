import { useState } from "react";
import NewExpense from "./components/NewExpense/NewExpense"
import Expenses from './components/Expenses/Expenses'

const expenses_dummy = [
  {
    id: 'e1',
    title: 'Toilet Paper',
    amount: 94.12,
    date: new Date(2020, 7, 14),
  },
  { id: 'e2', title: 'New TV', amount: 799.49, date: new Date(2021, 2, 12) },
  {
    id: 'e3',
    title: 'Car Insurance',
    amount: 294.67,
    date: new Date(2021, 2, 28),
  },
  {
    id: 'e4',
    title: 'New Desk (Wooden)',
    amount: 450,
    date: new Date(2021, 5, 12),
  }
];
function App() {

  const [expi, setExpi] = useState(expenses_dummy);
  const getdata = (Dataa) => {
    setExpi((PrevExpi) => {
      return [ Dataa,...PrevExpi];
    });

  };
  return (
    <div>
      <NewExpense DataGet={getdata}></NewExpense>
      <Expenses expen={expi}></Expenses>
    </div>
  );
}

export default App;
