interface Props{
    item:any;
}

export default function HistoryRow({
    item,
}:Props){

    return(

        <tr className="border-b">

            <td className="p-4">
                {item.id}
            </td>

            <td className="p-4">
                {item.goal}
            </td>

            <td className="p-4">
                {item.ats_score}
            </td>

            <td className="p-4">
                {item.created_at}
            </td>

        </tr>

    );

}