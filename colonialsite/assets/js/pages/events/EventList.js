import React from 'react';
import Event from './Event.js';
import EventFilterTable from './EventFilterTable.js';
import EventDetail from './EventDetail';
import EventDetailModal from './EventDetailModal';

function sortByDate(a, b){
    a = new Date(a.start_date);
    b = new Date(b.start_date);
    return a>b ? 1 : a<b ? -1 : 0;
}

function sortByType(a, b){
    a = a.category;
    b = b.category;
    return a>b ? -1 : a<b ? 1 : 0;
}
function sortByLocation(a, b){
    a = a.location;
    b = b.location;
    return a>b ? -1 : a<b ? 1 : 0;
}

var EventList = React.createClass({
    loadContentFromServer: function(){
        $.ajax({
            url:this.props.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data:data.results})
                this.updateFilters(this.state.types, true);
                this.updateSort("Date");
            }.bind(this)
        })
    },

    isFuture: function(event){
        var now = new Date();
        var date = new Date(event.start_date);
        return date > now;
    },

    getInitialState: function() {
        return {data: [], filtered_data:[],
            types:
            [
            {id:"IMs", selected:true},
            {id:"Friday Party", selected:true},
            {id:"Semiformal", selected:true},
            {id:"Study Break", selected:true},
            {id:"Sophomore Dinner", selected:true},
            {id:"Language Table", selected:true},
            {id:"Other", selected:true}
            ],
            sortTypes:
            [
            {id:"Date"},
            {id:"Category"},
            {id:"Location"}
            ],
            defaultSort:"Date"
        }
    },

    componentDidMount: function() {
        this.loadContentFromServer();
        setInterval(this.loadContentFromServer,
            this.props.pollInterval)
    },
    updateFilters: function(types, excludePast) {
        //Types selected is a list of all the types of events that we want to include in the filtered_data
        var types_selected = types.filter(function (type){
            return type.selected;
        });
        this.setState({filtered_data:
            this.state.data.reduce(function(events_selected, event){
                var hits = types_selected.filter(function(event_type){
                    return event_type.id === event.category;
                });
                if (hits.length > 0) {
                    if ((!excludePast || this.isFuture(event)) && event.status === "Open")
                        events_selected.push(event);
                }
                return events_selected;
            }.bind(this), [])});
    },
    updateSort: function(sortType){
        var sortFunction;
        switch(sortType){
            case "Category":
                sortFunction = sortByType;
                break;
            case "Location":
                sortFunction = sortByLocation;
                break;
            default:
                sortFunction = sortByDate;
        }
        this.setState({filtered_data:
            this.state.filtered_data.sort(sortFunction)
        });
    },
    renderDetail: function(id) {
      this.setState({event: this.state.filtered_data.find(event => event.pk == id), showModal:true})
    },
    render: function() {
        return (
                <div>
                    <div className="container col-md-12 col-sm-12 col-xs-12 col-lg-6">
                     <div className='scroll-container-header border-bottom-1'> Events: </div>
                        <EventFilterTable   events={this.state.filtered_data}
                                            types={this.state.types}
                                            updateFilteredList={this.updateFilters}
                                            updateSort={this.updateSort}
                                            sortTypes={this.state.sortTypes}
                                            renderDetail={this.renderDetail}
                                            selected_event={this.state.event}
                                            defaultSort={this.state.defaultSort} />
                    </div>
                    <div className="container col-lg-6 hidden-md hidden-sm hidden-xs">
                        <EventDetail key={"Large screen"}
                                     activeEvent={this.state.event} />
                    </div>
                    <div className="container">
                        <EventDetailModal key={"smallScreen"}
                                          activeEvent={this.state.event}
                                          showModal={this.state.showModal && window.innerWidth < 1200}
                                          onHide={() => this.setState({ showModal: false})} />
                    </div>
                </div>
               )
    }
});

export default EventList;
