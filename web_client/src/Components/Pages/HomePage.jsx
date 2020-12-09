import React from "react"
import {makeStyles} from "@material-ui/core/styles"
import {Typography} from "@material-ui/core"

const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex',
        flexDirection: 'column'
    },
}))

export default function HomePage() {
    const classes = useStyles()

    return (
        <div className={classes.root}>
            <Typography variant='h6'>
                Home page
            </Typography>
        </div>
    )
}
