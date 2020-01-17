import React, { useState, useCallback } from "react";
import { PageHeader, ListGroup, ListGroupItem } from "react-bootstrap";
import "./Home.css";

const STATUS = {
  'clockIn': 'Clock In',
  'clockOut': 'Clock Out',
}

export default function Home(props) {

  function renderLander() {
    return (
      <div className="lander">
        <h1>Welcome!</h1>
        <p>Please Log In</p>
      </div>
    );
  }

  const [status, setStatus] = useState('clockIn')
  const [clockList, setClockList] = useState([])

  const handleClock = useCallback(() => {
    if (status === 'clockIn') {
      setStatus('clockOut')
    } else {
      setStatus('clockIn')
    }
    setClockList([...clockList, {
      time: new Date(),
      type: status,
    }])
  }, [setClockList, status, setStatus, clockList])

  function renderEvents() {
    return (
      <div className="events">
        <div id="inputForm">
          <button type="button" onClick={handleClock}>{STATUS[status]}</button>
        </div>
        <PageHeader>Your Clock Events History</PageHeader>
        <ListGroup>
          {clockList.map(clockItem =>
            <div key={clockItem.time} className={clockItem.type === 'clockIn' ? 'clockInEvent' : 'clockOutEvent'}>
              <div class="column">
                <div className="leftgrid">Dummy UserName</div>
                <div className="middlegrid">{clockItem.time.toLocaleDateString()} {clockItem.time.toLocaleTimeString()} </div>
                <div className="rightgrid">{STATUS[clockItem.type]}</div>
              </div>
            </div>
          )}
        </ListGroup>
      </div>
    );
  }

  return (
    <div className="Home">
      {props.isAuthenticated ? renderEvents() : renderLander()}
    </div>
  );
}
