import React from "react"
import {makeStyles} from "@material-ui/core/styles"
import {Typography} from "@material-ui/core"

const useStyles = makeStyles((theme) => ({
    root: {
        maxWidth: '100%',
        display: 'flex',
        flexDirection: 'column'
    },
}))

export default function StatisticsPage() {
    const classes = useStyles()

    return (
        <div className={classes.root}>
            <Typography variant='h6'>
                StatisticsPage
            </Typography>
        </div>
    )
}
