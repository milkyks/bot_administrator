import React, {useState} from "react"
import {makeStyles} from "@material-ui/core/styles"
import {CardContent, Divider, Typography} from "@material-ui/core"
import Card from "@material-ui/core/Card"
import Switch from "@material-ui/core/Switch";
import CardActions from "@material-ui/core/CardActions";
import Button from "@material-ui/core/Button";
import ListItem from "@material-ui/core/ListItem";
import List from "@material-ui/core/List";
import Chip from "@material-ui/core/Chip";
import clsx from "clsx";
import IconButton from "@material-ui/core/IconButton";
import ExpandMoreIcon from '@material-ui/icons/ExpandMore'
import Collapse from "@material-ui/core/Collapse";

const useStyles = makeStyles((theme) => ({
    root: {
        padding: theme.spacing(2),
        marginTop: theme.spacing(1),
        marginBottom: theme.spacing(1)
    },
    header: {
        display: "flex",
        alignItems: "center"
    },
    title: {
        marginRight: theme.spacing(1)
    },
    content: {
        paddingLeft: 0,
        paddingRight: 0,
    },
    contentSubtitle: {
        marginTop: theme.spacing(2)
    },
    actions: {
        paddingLeft: 0,
        paddingRight: 0,
    },
    synonyms: {
        display: 'flex',
        flexWrap: 'wrap',
        '& > *': {
            margin: theme.spacing(1),
        },
    },
    response: {
        display: 'flex',
        overflow: 'auto',
        paddingLeft: theme.spacing(1),
        paddingRight: theme.spacing(1)
    },
    responseText: {
        whiteSpace: 'pre-line'
    },
    active: {
        marginRight: theme.spacing(2)
    },
    expand: {
        transform: 'rotate(0deg)',
        marginLeft: 'auto',
        transition: theme.transitions.create('transform', {
            duration: theme.transitions.duration.shortest,
        }),
    },
    expandOpen: {
        transform: 'rotate(180deg)',
    },
}))

export default function Command({mainName, isActive, priority, synonyms, responses}) {
    const classes = useStyles()

    const [expanded, setExpanded] = useState(false)

    const changeActive = (event) => {
        //!
        console.log(event.target.checked)
    }

    return (
        <Card variant="outlined" className={classes.root}>
            <div className={classes.header}>
                <Switch
                    color='primary'
                    className={classes.active}
                    checked={isActive}
                    onChange={changeActive}
                />
                <Typography className={classes.title} variant='h6'>
                    {mainName}
                </Typography>
                <Typography color='textSecondary' variant="subtitle2">
                    {priority}
                </Typography>
                <IconButton
                    className={clsx(classes.expand, {
                        [classes.expandOpen]: expanded,
                    })}
                    onClick={() => setExpanded(!expanded)}
                >
                    <ExpandMoreIcon />
                </IconButton>
            </div>

            <Collapse in={expanded}>
                <CardContent className={classes.content}>
                    <Typography className={classes.contentSubtitle} variant="subtitle2">
                        Синонимы
                    </Typography>
                    <div className={classes.synonyms}>
                        {synonyms.map(synonym =>
                            <Chip label={synonym} key={synonym}/>
                        )}
                    </div>

                    <Typography className={classes.contentSubtitle} variant="subtitle2">
                        Ответы
                    </Typography>
                    <List>
                        {responses.map((response, index) =>
                            <div key={response}>
                                <ListItem className={classes.response}>
                                    <Typography className={classes.responseText}>
                                        {response}
                                    </Typography>
                                </ListItem>
                                {index !== responses.length - 1 && <Divider/>}
                            </div>
                        )}
                    </List>
                </CardContent>
            </Collapse>

            <CardActions className={classes.actions}>
                <Button
                    // startIcon={<EditRounded/>}
                >
                    Редактировать
                </Button>
                <Button
                    // startIcon={<DeleteOutlineRounded/>}
                >
                    Удалить
                </Button>
            </CardActions>
        </Card>
    )
}