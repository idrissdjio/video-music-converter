import pika, json
import traceback

def upload(f, fs, channel, access):
    try:
        # Store file in GridFS
        fid = fs.put(f)
    except Exception as err:
        print("Error storing file in GridFS:", str(err), traceback.format_exc())
        return "Error storing file", 500

    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }

    try:
        # Publish message to RabbitMQ
        channel.basic_publish(
            exchange="",
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
    except Exception as err:
        print("Error publishing to RabbitMQ:", str(err), traceback.format_exc())
        fs.delete(fid)  # Clean-up by removing file from GridFS if publish fails
        return "Error sending message", 500

    return None  # No error