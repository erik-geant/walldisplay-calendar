import React, {useEffect} from 'react';
// import { formatDistance } from 'date-fns';
import {
    Calendar,
    Views,
    // DateLocalizer,
    momentLocalizer,
  } from 'react-big-calendar'
import "./styles.scss"
// import PropTypes from 'prop-types'
import moment from 'moment'

const events_url = "http://localhost:33333/api/events";

// interface Event {
//     id: string;
//     data1: string;
//     data2: string;
//     data3: string;
//     state: boolean;
//     time: number;
// }


// export interface IAppProps {
//     refresh_frequency_ms?: number;
//     api_url?: string;
// }

// function timeFormatter(time: number, _thing: Thing): string {
//     return formatDistance(new Date(1000 * time), new Date());
// }

// const columns = [
//     {
//         dataField: 'state',
//         text: 'State'
//     },
//     {
//         dataField: 'data1',
//         text: 'Data 1'
//         // title: columnTitle
//     }, {
//         dataField: 'data2',
//         text: 'Data 2'
//     }, {
//         dataField: 'data3',
//         text: 'Data 3',
//         // classes: severityClasses,
//         // formatter: severityFormatter
//     }, {
//         dataField: 'time',
//         text: 'When',
//         formatter: timeFormatter
//     }
// ];


// const ThingRow = (t: Thing): Thing => {
//     return {
//         id: t.id,
//         time: t.time,
//         state: t.state,
//         data1: t.data1,
//         data2: t.data2,
//         data3: t.data3
//     }
// }


// const rowClass = (row: Thing, _rowIndex: number): string => {
//     if (row.state)
//         return 'state_true';
//     else
//         return 'state_false';
// }



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

// const the_localizer = PropTypes.instanceOf(DateLocalizer);
const the_localizer = momentLocalizer(moment);


// const ColoredDateCellWrapper = (children: any) =>
//   React.cloneElement(React.Children.only(children), {
//     style: {
//       backgroundColor: 'lightblue',
//     },
//   })

// const the_components = {
//     timeSlotWrapper: ColoredDateCellWrapper,
// };

const the_views = [Views.MONTH, Views.WEEK, Views.DAY];

// const { components, defaultDate, max, views } = useMemo(
//     () => ({
//       components: {
//         timeSlotWrapper: ColoredDateCellWrapper,
//       },
//       defaultDate: new Date(2015, 3, 1),
//       max: dates.add(dates.endOf(new Date(2015, 17, 1), 'day'), -1, 'hours'),
//       views: Object.keys(Views).map((k) => Views[k]),
//     }),
//     []
//   )


const Events: React.FC = () => {

    const [events, setEvents] = React.useState<Event[]>([]);
    
    console.log('re-rendering Calendar')

    useEffect(() => {

        async function loadEvents() {
            // console.log('starting loadEvents(), source: "' + props.api_url + '"');
            
            // api_uri shouldn't be undefined, since
            // there's a default value - but TypeScript can't see
            // this, apparently (?)
            const response = await fetch(events_url);
            const rsp_json = await response.json();
            setEvents(rsp_json.map((e: InputEvent) => make_event(e)));
        }

        loadEvents();
        setInterval(loadEvents, 60000);

    }, []);

    return <div className="height600">
        <Calendar
            // components={the_components}
            events={events}
            localizer={the_localizer}
            views={the_views}
        />
    </div>;
};

export default Events;
