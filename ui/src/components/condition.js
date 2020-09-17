import React from "react";
import CustomSelect from "./CustomSelect";

const nutrientOptions = [{
    label: "Protein",
    value: 203,
    unit: "g"
}, {
    label: "Fat",
    value: 204,
    unit: "g"
}, {
    label: "Carbohydrate, by difference",
    value: 205,
    unit: "g"
}, {
    label: "Sugar",
    value: 269,
    unit: "g"
}];

const operatorOptions = [{
    label: "=",
    value: "="
}, {
    label: ">",
    value: ">"
}, {
    label: "<",
    value: "<"
}, {
    label: ">=",
    value: ">="
}, {
    label: "<=",
    value: "<="
}];

const chainerOptions = [{
    label: "and",
    value: "and"
}, {
    label: "or",
    value: "or"
}];

const style = {
    paddingTop: "16px",
    display: "flex",
    flexDirection: "column",
    minWidth: "300px"
}

const selectionStyle = {
    width: "100%"
}


const Condition = (props) => {
    const {condition: c, updateConditions, removeCondition, onSelectedOperator} = props

    return (<div className="condition" style={style}>
        <div className="condition-selections" style={selectionStyle}>
            {c.id > 1 &&
            <button style={{display: "inline-block"}} onClick={() => removeCondition(c)}>
                x
            </button>
            }
            <CustomSelect
                onChange={(selected) => {
                    c.nutrient = selected;
                    updateConditions(c);
                }}
                options={nutrientOptions}
                width={"40%"}
                value={c.nutrient}
            />
            <CustomSelect
                onChange={(selected) => {
                    c.operator = selected;
                    updateConditions(c);
                }}
                options={operatorOptions}
                width={"15%"}
                value={c.operator}
            />
            <input
                type="number"
                value={c.value}
                style={{
                    display: "inline-block",
                    width: "20%",
                    height: "34px",
                    borderColor: "hsl(0,0%,80%)",
                    borderRadius: "4px",
                    borderStyle: "solid",
                    borderWidth: "1px",
                    margin: "5px"
                }}
                onChange={(e) => {
                    c.value = Number(e.target.value);
                    return updateConditions(c);
                }}/>
            {/*{c.unit}*/}
        </div>
        <CustomSelect
            onChange={(selected) => {
                c.chain_operator = selected;
                onSelectedOperator(c.id)
                updateConditions(c);
            }}
            width={"50%"}
            margin={"0 auto"}
            styles={{width: "50%"}}
            options={chainerOptions}
            value={c.chain_operator}
            placeholder={"Add condition..."}
        />
    </div>);
};

export default Condition;
