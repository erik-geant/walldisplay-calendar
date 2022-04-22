import React, {useEffect} from 'react';
import {
    Calendar,
    Views,
    momentLocalizer,
  } from 'react-big-calendar'
import "./styles.scss"
import moment from 'moment'

const EVENTS_API_ENDPOINT = "api/events";

export interface IAppProps {
    api_uri_base: string;
    refresh_ms: number;
}

interface Event {
    id: number;
    title: string;
    start: Date;
    end: Date;
}

interface InputEvent {
    id: number;
    title: string;
    startDate: string;
    endDate: string;
    timezone: string;
    url: string;
}

const make_event = (e: InputEvent): Event => {
    return {
        id: e.id,
        title: e.title,
        start: new Date(e.startDate),
        end: new Date(e.endDate)
    };
};

const the_localizer = momentLocalizer(moment);
const the_views = [Views.MONTH];
// const the_views = [Views.MONTH, Views.WEEK, Views.DAY];
const Events: React.FC<IAppProps> = (props) => {

    const [events, setEvents] = React.useState<Event[]>([]);
    
    console.log('re-rendering Calendar')

    useEffect(() => {

        function reload() {
            window.location.reload();
        }

        async function loadEvents() {
            const response = await fetch(props.api_uri_base + EVENTS_API_ENDPOINT);
            const rsp_json = await response.json();
            setEvents(rsp_json.map((e: InputEvent) => make_event(e)));
        }

        loadEvents();
        setInterval(reload, props.refresh_ms);
    }, [props.refresh_ms, props.api_uri_base]);

    return <div className="height600">
        <Calendar
            // components={the_components}
            events={events}
            localizer={the_localizer}
            views={the_views}
            // toolbar={false}
        />
    </div>;
};

export default Events;
