import React from 'react';
import {DropdownButton, MenuItem, Glyphicon} from 'react-bootstrap';
class EventFilterDropdown extends React.Component{
	
	constructor(props) {
		super(props);
		this.state=
		{
			types:this.props.types
		};
	}

	changeSelection(id) {
		var types_selected = this.state.types.map(function(d) {
			return {
				id:d.id,
				selected: (d.id == id ? !d.selected : d.selected)
			}
		})
		this.setState({ types: types_selected });
		this.props.updateFilteredList(types_selected);
	}

	render(){
		var checks = this.state.types.map(function(d) {
			return (
					<MenuItem> <input type="checkbox" checked={d.selected} onChange={this.changeSelection.bind(this, d.id)} />
					{d.id}
					</MenuItem>
				);
		}.bind(this));

		return(
			<DropdownButton title={<Glyphicon glyph="filter"/>}>
			{checks}	
			</DropdownButton>	
		)
	}
}
export default EventFilterDropdown;