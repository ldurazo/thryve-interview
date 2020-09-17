import React from "react";
import Select from "react-select";

const CustomSelect = (props) => {
    const {onChange, options, width, value, margin, placeholder} = props
    return <div style={{ display: 'inline-block', width, padding: "5px", margin}}>
        <Select
            options={options}
            components={{DropdownIndicator: () => null, IndicatorSeparator: () => null}}
            value={value}
            onChange={onChange}
            placeholder={placeholder}
        />
    </div>;
};

export default CustomSelect;
