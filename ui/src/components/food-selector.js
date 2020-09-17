import React, {Fragment, useEffect, useState} from "react";
import Condition from "./condition";

const selectionBlueprint = {
    "nutrient": {value: 203, label: "Protein"},
    "operator": {value: ">", label: ">"},
    "unit": "g",
    "value": 0,
};

const style = {
    display: "flex",
    height: "100%",
}

const ulStyle = {
    listStyle: "none",
    maxHeight: "800px",
    margin: "16px auto",
    padding: "20px",
    overflowY: "scroll",
    borderColor: "hsl(0,0%,80%)",
    borderRadius: "4px",
    borderStyle: "solid",
    borderWidth: "1px",
}

const liStyle = {
    textAlign: "left",
    overflowX: "hidden",
    paddingBottom: "10px",
}

const conditionsStyle = {
    margin: "16px",
    borderColor: "hsl(0,0%,80%)",
    borderRadius: "4px",
    borderStyle: "solid",
    borderWidth: "1px",
}

const FoodSelector = () => {
    const defaultSelection = {...selectionBlueprint, "id": 1};
    const [conditions, setConditions] = useState([defaultSelection]);
    const [foods, setFoods] = useState([]);

    const formatConditions = () => {
        return conditions.map(c => {
            return {
                nutrient: c.nutrient.value,
                operator: c.operator.value,
                unit: c.nutrient.unit,
                value: c.value,
                chain_operator: c.chain_operator && c.chain_operator.value,
            }
        })
    }

    const fetchFoods = async () => {
        const apiUrl = "http://127.0.0.1:5000/foods";
        const response = await fetch(apiUrl, {
            method: "POST",
            mode: "cors",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formatConditions()),
        });
        return response.json();
    };

    useEffect(() => {
        fetchFoods().then(r => {
            setFoods(r);
        }).catch((e) => console.log(e));
    }, [conditions])

    const addNutrientCriteria = (idx) => {
        if (idx === conditions.length) {
            const defaultSelection = {...selectionBlueprint, "id": conditions.length + 1};
            conditions.push(defaultSelection);
        }
        setConditions([...conditions]);
    }

    const onConditionChange = (updatedCondition) => {
        const indexToUpdate = conditions.findIndex((c) => c.id === updatedCondition.id)
        if (indexToUpdate !== -1) {
            conditions[indexToUpdate] = updatedCondition;
        }
        setConditions([...conditions]);
    }

    const onConditionRemove = (condition) => {
        const indexToRemove = conditions.findIndex((c) => c.id === condition.id)
        if (indexToRemove !== -1) {
            conditions.splice(indexToRemove, 1);
        }
        setConditions([...conditions]);
    }

    return (<Fragment>
        <div className="food-selector" style={style}>
            <div className="conditions-container" style={conditionsStyle}>
                {conditions.map((c, index) =>
                    <Condition
                        key={index}
                        condition={c}
                        updateConditions={onConditionChange}
                        removeCondition={onConditionRemove}
                        onSelectedOperator={addNutrientCriteria}
                    />
                )}
            </div>
            <ul style={ulStyle}>
                {foods && foods.length > 0 ?
                    foods.map((f, i) => <li key={i} style={liStyle}>{f}</li>) :
                    <p>No results found</p>
                }
            </ul>
        </div>
    </Fragment>);
};

export default FoodSelector;
