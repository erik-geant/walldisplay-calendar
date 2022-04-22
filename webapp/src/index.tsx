import React from "react";
import ReactDOM from "react-dom";
import Events from "./Events"

const query = new URLSearchParams(window.location.search);

if (query.has('test'))
  ReactDOM.render(
    <Events 
      api_uri_base='http://localhost:33333/'
      refresh_ms={60*1000}
    />,
    document.getElementById("root") as HTMLElement);
else
  ReactDOM.render(
    <Events 
      api_uri_base={window.location.origin}
      refresh_ms={12*3600*1000}
    />,
    document.getElementById("root") as HTMLElement);
