import { Injectable, InternalServerErrorException } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { MessageDoc, Message } from './models/message.model';
import { Model } from 'mongoose';
import { CreateMessageDto } from './dto/create-message.dto';

@Injectable()
export class MessagesService {
  constructor(
    @InjectModel(Message.name) private messageModel: Model<MessageDoc>,
  ) {}
  async findAll() {
    try {
      const messages = await this.messageModel.find();
      return messages;
    } catch (error) {
      throw new InternalServerErrorException(error);
    }
  }

  async createMessage(createMessageDto: CreateMessageDto) {
    try {
      const doc = new this.messageModel(createMessageDto);
      const message = await doc.save();
      return message;
    } catch (error) {
      console.log(error);
      throw new InternalServerErrorException(error);
    }
  }
  async deleteAll() {
    try {
      const result = await this.messageModel.deleteMany({});
      return { success: true, deletedCount: result.deletedCount };
    } catch (error) {
      console.log(error);
      throw new InternalServerErrorException(error);
    }
  }
}
