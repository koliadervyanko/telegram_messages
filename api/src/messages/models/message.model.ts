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
    default: null,
  })
  replies: Message[] | null;

  @Prop({ required: true })
  messageId: number;

  @Prop({ required: true })
  keyWord: string;

  @Prop({ default: null, type: { ...Message } })
  repliedTo: object | null;
}

export const MessagesSchema = SchemaFactory.createForClass(Message);
