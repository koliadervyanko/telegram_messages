import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { Document, Schema as MongooseSchema } from 'mongoose';

export type MessageDoc = Message & Document;

@Schema()
export class Message {
  @Prop()
  username: string | null;

  @Prop({ required: true })
  message: string;

  @Prop()
  name: string;

  @Prop({ required: true })
  link: string;

  @Prop({ required: true })
  date: string;

  @Prop({
    type: [{ type: MongooseSchema.Types.ObjectId, ref: 'Message' }],
    default: null,
  })
  replies: Message[] | null;

  @Prop({ required: true })
  messageId: number;

  @Prop({ required: true })
  keyWord: string;

  @Prop({ type: MongooseSchema.Types.ObjectId, ref: 'Message', default: null })
  replyTo: Message | null;
}

export const MessagesSchema = SchemaFactory.createForClass(Message);
