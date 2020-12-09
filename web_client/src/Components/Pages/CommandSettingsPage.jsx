import React, {useEffect} from "react"
import {makeStyles} from "@material-ui/core/styles"
import {Typography} from "@material-ui/core"
import {useDispatch, useSelector} from "react-redux";
import {fetchCommands, selectAllCommands} from "../../slices/commandsSlice";
import CircularProgress from "@material-ui/core/CircularProgress";
import Command from "../Command";

const useStyles = makeStyles((theme) => ({
    root: {
        maxWidth: '100%',
        display: "flex",
        flexDirection: 'column',
    },
    info: {
        marginBottom: theme.spacing(4)
    }
}))

export default function CommandSettingsPage() {
    const classes = useStyles()
    const dispatch = useDispatch()

    const commands = useSelector(selectAllCommands)
    const commandsStatus = useSelector(state => state.commands.status)

    useEffect(() => {
        if (commandsStatus === 'idle') {
            dispatch(fetchCommands())
        }
    }, [commandsStatus, dispatch])

    return (
        <div className={classes.root}>
            <Typography className={classes.info}>
                На этой странице можно создать новые команды для бота, настроить уже существующие.
            </Typography>

            {commandsStatus === 'loading' && <CircularProgress/>}
            {commandsStatus === 'succeeded' && commands.map(command =>
                <Command
                    mainName={command.mainName}
                    isActive={command.isActive}
                    priority={command.priority}
                    synonyms={command.synonyms}
                    responses={command.responses}
                />
            )}
        </div>
    )
}
