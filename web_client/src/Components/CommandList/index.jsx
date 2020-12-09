import React from 'react'
import List from "@material-ui/core/List"
import ListItem from "@material-ui/core/ListItem"
import ListItemText from "@material-ui/core/ListItemText"
import {makeStyles} from "@material-ui/core/styles"

const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex',
        flexDirection: 'column',
    }
}))

export default function CommandList({commands}) {
    const classes = useStyles()

    return (
        <div className={classes.root}>
            <List>
                {commands.map(command =>
                    <ListItem key={command.id}>
                        <ListItemText
                            primary={`id ${command.id}`}
                            secondary={command.text}
                        />
                    </ListItem>
                )}
            </List>
        </div>
    )
}
